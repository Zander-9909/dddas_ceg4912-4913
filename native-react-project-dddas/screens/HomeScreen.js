import React from 'react';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';


function HomeScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Home screen</Text>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#e8bcf0'
    },
})

export default HomeScreen;