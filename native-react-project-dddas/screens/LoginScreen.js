import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';

function LoginScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the login screen for the DDDAS project</Text>
            <StatusBar style="auto" />
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
})

export default LoginScreen;