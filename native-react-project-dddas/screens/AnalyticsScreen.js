import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Dimensions, LogBox } from 'react-native';
import { PieChart, LineChart } from 'react-native-chart-kit';
import axios from 'axios';
import * as Notifications from 'expo-notifications';
const screenWidth = Dimensions.get('window').width;
const screenHeight = Dimensions.get('window').height;
import { Audio } from 'expo-av';

async function registerForPushNotificationsAsync() {
  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') {
    alert('Sorry, we need notification permissions to make this work!');
    return;
  }
  // ...
}
LogBox.ignoreAllLogs();
async function scheduleRepeatingNotification() {
  await Notifications.scheduleNotificationAsync({
    content: {
      title: "Drowsiness Alert",
      body: 'You may feel drowsy, pull over soon!',
    },
    trigger: {
      seconds: 15, // 120 seconds = 2 minutes
      repeats: false
    },
  });
}

const AnalyticsScreen = () => {
  Notifications.setNotificationHandler({
    handleNotification: async () => ({
      shouldShowAlert: true,
      shouldPlaySound: true,
      shouldSetBadge: true,
    }),
  });
  async function loadSound() {
    const { sound } = await Audio.Sound.createAsync(
        require('C:/Users/downt/Documents/GitHub/dddas_ceg4912-4913/native-react-project-dddas/alarm.mp3')
    );
    setSound(sound);
  }
  const [sound, setSound] = useState();

  // State for Line Chart
  const [data, setData] = useState([0,5,6,7]);

  // State for Pie Chart
  const [pieChartData, setPieChartData] = useState([
    { name: 'Not Drowsy', population: 0, color: '#000000', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'Slightly Drowsy', population: 0, color: '#4a1782', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'Drowsy', population: 0, color: '#9f80d1', legendFontColor: '#7F7F7F', legendFontSize: 15 },
  ]);
  useEffect(() => {
    loadSound();
    const interval = setInterval(() => {
      axios.get(`http://100.72.37.45:5000/webhook`).then((response) => {
        console.log(response.data);
        //scheduleRepeatingNotification();
        const newValue = response.data.heartrate
        setData(currentData => [...currentData, newValue].slice(-11));
        const newData = [...pieChartData];
        newData[response.data.results].population += 1;
        setPieChartData(newData);
        if (response.data.alert == true){
          registerForPushNotificationsAsync();
          scheduleRepeatingNotification();
          //console.log("printing")
          sound && sound.playAsync();
        }
      });

    }, 10000); // Update interval for both charts

    return () => {
      //sound && sound.unloadAsync();
      clearInterval(interval);
  };
}, [pieChartData]);
  //[pieChartData, sound]);

  const lineChartData = {
    labels: data.map((_, index) => String(index)),
    datasets: [{ data: data }],
  };

  const pieChartConfig = {
    backgroundColor: '#ffffff',
    backgroundGradientFrom: '#ffffff',
    backgroundGradientTo: '#ffffff',
    decimalPlaces: 2,
    color: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
    style: { borderRadius: 16 },
    labelColor: (opacity = 0) => `rgba(0, 0, 0, ${opacity})`, // This will make the labels transparent
  };

  const lineChartConfig = {
    backgroundColor: '#000080',
    backgroundGradientFrom: '#000080',
    backgroundGradientTo: '#000080',
    decimalPlaces: 2,
    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
    style: { borderRadius: 16 },
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Drowsiness Levels</Text>
      <PieChart
        data={pieChartData}
        width={screenWidth}
        height={220}
        chartConfig={pieChartConfig}
        accessor={'population'}
        backgroundColor={'transparent'}
        paddingLeft={'15'}
        center={[10, 10]}
        absolute={false}
      />

      <LineChart
        data={lineChartData}
        width={screenWidth}
        height={screenHeight / 2} // Adjust height as needed
        chartConfig={lineChartConfig}
        bezier
        style={{
          marginVertical: 8,
          borderRadius: 16
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  header: {
    fontSize: 20,
    marginBottom: 10,
  },
});

export default AnalyticsScreen;
