import React from 'react';
import { StyleSheet, View } from 'react-native';

function LoginScreen(props) {
    return (
        <View style={styles.background}>
            <Text>This is the front end for the DDDAS project in Native React.</Text>
            <StatusBar style="auto" />
        </View>
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