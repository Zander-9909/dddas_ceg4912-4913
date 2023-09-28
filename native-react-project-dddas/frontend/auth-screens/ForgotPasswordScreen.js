import React from 'react';
import {
    StyleSheet, Text, SafeAreaView, TouchableWithoutFeedback, KeyboardAvoidingView,
    StatusBar, Keyboard, View, TextInput, Button
} from 'react-native';

function ForgotPasswordScreen(props) {

    const [username, OnChangeUsername] = React.useState('');

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
            style={styles.container}>
            <StatusBar backgroundColor='#FFFFFF' barStyle='dark-content' />

            <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                <View style={styles.inner}>

                    <View style={styles.inputContainer}>
                        <TextInput
                            style={[styles.textInput, styles.buttonMargin]}
                            onChangeText={OnChangeUsername}
                            value={username}
                            placeholder='Username'

                            secureTextEntry={true}
                            keyboardType='default'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
                        <Button
                            color='blue'
                            onPress={() => handleFP(username)}
                            title='RECOVER PASSWORD'
                        />
                    </View>

                </View>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        // paddingTop: StatusBar.currentHeight,
    },
    inner: { 
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    inputContainer: {
        // flex: 6,
        alignItems: 'center',
    },
    textInput: { 
        width: 200,
        height: 35,
        borderColor: '#000000',
        borderBottomWidth: 1,
    },

})
export default ForgotPasswordScreen;