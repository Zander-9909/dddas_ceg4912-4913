import React from 'react';
import { StyleSheet, Text, SafeAreaView, Button } from 'react-native';

// screen names
const forgotPasswordName = 'ForgotPassword';
const registerName = 'Register';
const navigationName = 'Navigation';

function LoginScreen(props) {
    const { navigation } = props;
    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Login screen</Text>

            <Button
                onPress={() => navigation.navigate(navigationName)}
                title="Login"
                style={{}}
                // accessibilityLabel="Learn more about this purple button"
            />

            <Button
                onPress={() => navigation.navigate(registerName)}
                title="Register"
                style={{}}
                // accessibilityLabel="Learn more about this purple button"
            />

            <Button
                onPress={() => navigation.navigate(forgotPasswordName)}
                title="Forgot Password"
                style={{}}
                // accessibilityLabel="Learn more about this purple button"
            />
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