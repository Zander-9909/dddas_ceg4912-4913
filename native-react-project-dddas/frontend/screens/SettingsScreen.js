import React from 'react';
import { StyleSheet, Text, SafeAreaView, View, Button } from 'react-native';

// screens
const signinScreenName = 'Signin';

function SettingsScreen(props) {
    const { navigation } = props;

    return (
        <SafeAreaView style={styles.background}>

            <View style={styles.rect}></View>

            <TouchableOpacity
                onPress={() => navigation.navigate()}
                style={styles.rect}
            ></TouchableOpacity>

            <View style={styles.rect}></View>

            <View style={styles.rect}></View>

            <TouchableOpacity
                onPress={() => navigation.navigate(signinScreenName)}
                title='Sign out'
                style={styles.rect}
            ></TouchableOpacity>

        </SafeAreaView >
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    rect: {
        width: '90%',
        height: '3.5%',
        backgroundColor: "#E6E6E6",
    },  
})

export default SettingsScreen;