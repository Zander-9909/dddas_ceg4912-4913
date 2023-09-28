import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';

function AlertsScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Alert screen</Text>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
})

export default AlertsScreen;