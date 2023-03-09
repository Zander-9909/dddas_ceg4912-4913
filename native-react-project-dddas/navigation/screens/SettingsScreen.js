import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';

function AlertsScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Settings screen</Text>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#b5e7a0',
        alignItems: 'center',
        justifyContent: 'center',
    },
})

export default AlertsScreen;