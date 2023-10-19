import React, { useState, useEffect } from 'react'
import { StyleSheet, Text, View, SafeAreaView } from 'react-native'
import tw from 'tailwind-react-native-classnames';

const tableData = [
    ['Val', 'Mean', 'Max', 'Min'],
    ['EAR', '0.2884', '0.3326', '0.2439'],
    ['MAR', '0.9783', '1.1267', '0.7742'],
    ['CIR', '0.4388', '0.5493', '0.3383'],
    ['MOE', '3.3968', '4.3078', '2.7437'],
    ['TTP', '0.0014', '0.0018', '0.0013'],
    ['TTD', '0.0355', '0.0464', '0.0271'],
    ['TTC', '0.1459', '0.1942', '0.1353'],
];

const AnalyticsScreen = () => {

    return (
        <SafeAreaView>
            <SafeAreaView>
                <Text style={tw`text-3xl font-bold p-8`}>Statistics</Text>
                <View style={tw`p-4`}>
                    {tableData.map((row, rowIndex) => (
                        <View key={rowIndex} style={tw`flex flex-row justify-between`}>
                            {row.map((cell, cellIndex) => (
                                <Text key={cellIndex} style={tw`w-1/4 text-center`}>
                                    {cell}
                                </Text>
                            ))}
                        </View>
                    ))}
                </View>
            </SafeAreaView>
        </SafeAreaView>

    )
}
export default AnalyticsScreen
const styles = StyleSheet.create({})