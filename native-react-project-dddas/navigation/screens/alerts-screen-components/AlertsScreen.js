import React from 'react';
import { StyleSheet, Text, SafeAreaView, ScrollView } from 'react-native';

import AlertsScreenHeader from './AlertsScreenHeader'
import AlertComponent from './AlertContainer';

function AlertsScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
          <ScrollView style={styles.scrollViewStyle}>
            <AlertsScreenHeader></AlertsScreenHeader>
            <AlertComponent></AlertComponent>
          </ScrollView>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#66ccff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    scrollViewStyle: {
      marginVertical: '0%'
    }
})

export default AlertsScreen;