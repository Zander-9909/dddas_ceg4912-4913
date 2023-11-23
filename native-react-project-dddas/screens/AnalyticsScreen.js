import React, { useState, useEffect } from 'react';
import { LineChart } from 'react-native-chart-kit';
import { Dimensions } from 'react-native';

const screenWidth = Dimensions.get('window').width;
const screenHeight = Dimensions.get('window').height;

const AnalyticsScreen = () => {
  const [data, setData] = useState([1, 5, 8]);

  useEffect(() => {
    const interval = setInterval(() => {
      const newValue = Math.floor(Math.random() * 100) + 1;
      setData(currentData => [...currentData, newValue]);
    }, 10000); // 30000 milliseconds = 30 seconds

    return () => clearInterval(interval);
  }, []);

  const chartData = {
    labels: data.map((_, index) => String(index)),
    datasets: [{
      data: data
    }]
  };

  return (
    <LineChart
      data={chartData}
      width={screenWidth}
      height={screenHeight}
      chartConfig={{
        backgroundColor: '#e26a00',
        backgroundGradientFrom: '#fb8c00',
        backgroundGradientTo: '#ffa726',
        decimalPlaces: 2,
        color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
        style: {
          borderRadius: 16
        }
      }}
      bezier
      style={{
        marginVertical: 8,
        borderRadius: 16
      }}
    />
  );
};

export default AnalyticsScreen;
