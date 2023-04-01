import React from 'react';
import { StyleSheet, Text, SafeAreaView, View, TouchableOpacity } from 'react-native';
import Global from '../navigation/Global';


function SettingsScreen(props) {

    const { navigation } = props;

    return (
        <SafeAreaView style={styles.background}>
            <View style={styles.section}>
                <Text style={styles.sectionTitle}>Settings</Text>
            </View>

            <TouchableOpacity
                onPress={() => navigation.navigate(Global.cameraOutputName)}
                style={styles.button}>
                <Text style={styles.buttonText}>Configure Facial Detection</Text>
            </TouchableOpacity>

            <TouchableOpacity
                //   onPress={() => navigation.navigate(Global.)}
                style={styles.button}>
                <Text style={styles.buttonText}>Settings 1:</Text>
            </TouchableOpacity>

            <TouchableOpacity
                //   onPress={() => navigation.navigate(Global.)}
                style={styles.button}>
                <Text style={styles.buttonText}>Settings 2:</Text>
            </TouchableOpacity>

            <TouchableOpacity
                onPress={() => navigation.popToTop()}
                style={styles.button}>
                <Text style={styles.buttonText}>Sign Out</Text>
            </TouchableOpacity>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: '#fff',
    },
    section: {
        marginVertical: '5%',
    },
    sectionTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginHorizontal: '2%',
    },
    button: {
        backgroundColor: '#f2f2f2',
        paddingVertical: 20,
        paddingHorizontal: '5%',
        marginVertical: '1%',
        marginHorizontal: '2%%',
        borderRadius: 10,
    },
    buttonText: {
        fontSize: 16,
        textAlign: 'left',
    },
});



export default SettingsScreen;