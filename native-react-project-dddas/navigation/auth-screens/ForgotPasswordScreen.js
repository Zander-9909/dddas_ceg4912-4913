import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';

function ForgotPasswordScreen(props) {
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the ForgotPassword screen </Text>
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
export default ForgotPasswordScreen;