import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Dimensions } from 'react-native';
import { PieChart, LineChart } from 'react-native-chart-kit';
import axios from 'axios';
import * as Notifications from 'expo-notifications';
const screenWidth = Dimensions.get('window').width;
const screenHeight = Dimensions.get('window').height;
async function registerForPushNotificationsAsync() {
  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') {
    alert('Sorry, we need notification permissions to make this work!');
    return;
  }
  // ...
}

async function scheduleRepeatingNotification() {
  await Notifications.scheduleNotificationAsync({
    content: {
      title: "Test123",
      body: 'This is a test notification.',
    },
    trigger: {
      seconds: 15, // 120 seconds = 2 minutes
      repeats: false
    },
  });
}

const AnalyticsScreen = () => {

  // State for Line Chart
  const [data, setData] = useState([0]);

  // State for Pie Chart
  const [pieChartData, setPieChartData] = useState([
    { name: 'Not Drowsy', population: 0, color: 'green', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'Slightly Drowsy', population: 0, color: 'yellow', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'Drowsy', population: 0, color: 'red', legendFontColor: '#7F7F7F', legendFontSize: 15 },
  ]);

  useEffect(() => {
    registerForPushNotificationsAsync();
    const interval = setInterval(() => {
      axios.get(`http://100.72.37.45:5000/webhook`).then((response) => {
        console.log(response.data);
        //scheduleRepeatingNotification();
        const newValue = response.data.heartrate
        setData(currentData => [...currentData, newValue].slice(-11));
        const newData = [...pieChartData];
        newData[response.data.results].population += 1;
        setPieChartData(newData);
      });

    }, 1000); // Update interval for both charts

    return () => clearInterval(interval);
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
  };

  const lineChartConfig = {
    backgroundColor: '#e26a00',
    backgroundGradientFrom: '#fb8c00',
    backgroundGradientTo: '#ffa726',
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
        absolute
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
