import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Dimensions } from 'react-native';
import { PieChart, LineChart } from 'react-native-chart-kit';
import axios from 'axios';

const screenWidth = Dimensions.get('window').width;
const screenHeight = Dimensions.get('window').height;

const AnalyticsScreen = () => {
  // State for Line Chart
  const [data, setData] = useState([1, 5, 8]);

  // State for Pie Chart
  const [pieChartData, setPieChartData] = useState([
    { name: 'Alert', population: 0, color: 'green', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'A Little Sleepy', population: 0, color: 'yellow', legendFontColor: '#7F7F7F', legendFontSize: 15 },
    { name: 'Very Sleepy', population: 0, color: 'red', legendFontColor: '#7F7F7F', legendFontSize: 15 },
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      const baseUrl = 'https://reqres.in';
      axios.get(`${baseUrl}/api/users/1`).then((response) => {
        console.log(response.data);
      });
      const newValue = Math.floor(Math.random() * 100) + 1;
      setData(currentData => [...currentData, newValue]);
      
      const randomChoice = Math.floor(Math.random() * 3);
      const newData = [...pieChartData];
      newData[randomChoice].population += 1;
      setPieChartData(newData);
    }, 10000); // Update interval for both charts

    return () => clearInterval(interval);
  }, [pieChartData]);

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
      <Text style={styles.header}>Sleepiness Levels</Text>
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
