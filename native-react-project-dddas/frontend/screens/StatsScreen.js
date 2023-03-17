import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';

function StatsScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Stats screen</Text>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#f9ccac',
        alignItems: 'center',
        justifyContent: 'center',
    },
})

export default StatsScreen;