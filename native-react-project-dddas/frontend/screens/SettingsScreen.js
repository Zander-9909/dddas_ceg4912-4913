import React from 'react';
import { StyleSheet, Text, SafeAreaView, Button } from 'react-native';

// screens
const signinScreenName = 'Signin';

function SettingsScreen(props) {
    const { navigation } = props;

    return (
        <SafeAreaView style={styles.background}>
            <Text>This is the Settings screen</Text>

            <Button
                onPress={() => navigation.navigate(signinScreenName)}
                title='Sign out'
                style={{}}
                // accessibilityLabel="Learn more about this purple button"
            />
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

export default SettingsScreen;