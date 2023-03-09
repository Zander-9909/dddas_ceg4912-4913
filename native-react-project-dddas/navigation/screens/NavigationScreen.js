import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';


function NavigationScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Home screen</Text>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#e8bcf0',
        alignItems: 'center',
        justifyContent: 'center',
    },
})

export default NavigationScreen;