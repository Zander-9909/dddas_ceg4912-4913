import React from 'react';
import { StyleSheet, Text, SafeAreaView } from 'react-native';

function ForgotPasswordScreen(props) {
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
                            onChangeText={onChangePassword}
                            value={password}
                            placeholder='Password'

                            secureTextEntry={true}
                            keyboardType='default'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
                        <Button
                            color='blue'
                            onPress={() => handleRegister(username)}
                            title='RECOVER PASSWORD'
                        />
                    </View>

                </View>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
}

const styles = StyleSheet.create({
    container: { // for keyboard-avoiding-view
        // flex: 1,
        // paddingTop: StatusBar.currentHeight,
    },
    inner: { // for touchable-without-feedback inner-view
        // flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    inputContainer: { // for the 5 input fields
        // flex: 6,
        alignItems: 'center',
    },
    textInput: { // for username and password
        width: 200,
        height: 35,
        borderColor: '#000000',
        borderBottomWidth: 1,
    },
    
})
export default ForgotPasswordScreen;