import React from 'react';
import axios from 'axios';
import {
    StyleSheet, View, Text, TextInput, Button, Image, StatusBar, KeyboardAvoidingView,
    TouchableWithoutFeedback, Keyboard, TouchableOpacity
} from 'react-native';
import Logo from '../../assets/logo.png';

// screen names
const forgotPasswordName = 'ForgotPassword';
const registerName = 'Register';
const navigationName = 'Navigation';

function SigninScreen(props) {
    const { navigation } = props;
    const [username, onChangeUsername] = React.useState('');
    const [password, onChangePassword] = React.useState('');

    const handleSignin = async (inputUsername, inputPassword) => {
        const session_url = '/users/signin';
        const payload = {
            "username": inputUsername,
            "password": inputPassword
        };
    
        axios.post(session_url, payload)
            .then(response => {
                if (response.status === 200) { // signin successful
                    navigation.navigate(navigationName);
                } else { // signin failed
                    console.log('Signin failed');
                }
                console.log(response);
            })
            .catch(error => {
                console.log('Error', error.message);
            });
    };
    

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
            style={styles.container}>
            <StatusBar backgroundColor='#FFFFFF' barStyle='dark-content' />

            <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                <View style={styles.inner}>
                    <Image
                        style={styles.logo}
                        source={Logo}
                        resizeMode='contain'
                    />
                    <View style={{ marginBottom: '5%' }} >
                        <TextInput
                            style={styles.textInput}
                            onChangeText={onChangeUsername}
                            value={username}
                            placeholder='Username'

                            keyboardType='default'
                            autoCorrect={false}
                            spellCheck={false}
                            maxLength={20}
                        />

                        <TextInput
                            style={[styles.textInput, styles.textInputWithNoMarginBottom]}
                            onChangeText={onChangePassword}
                            value={password}
                            placeholder='Password'

                            keyboardType='default'
                            secureTextEntry={true}
                            autoCorrect={false}
                            spellCheck={false}
                            maxLength={20}
                        />

                        <TouchableOpacity style={{ alignSelf: 'flex-end' }} onPress={() => navigation.navigate(forgotPasswordName)}>
                            <Text style={{ fontSize: 18, color: 'blue' }}>Forgot password?</Text>
                        </TouchableOpacity>
                    </View>

                    <View style={{ marginBottom: '20%' }}>
                        <Button
                            color='blue'
                            onPress={() => handleSignin(username, password)}
                            title='Sign in'
                        />
                    </View>

                    <View style={{ flexDirection: 'row', justifyContent: 'center' }}>
                        <Text style={{ fontSize: 18 }}>Need an account? </Text>
                        <TouchableOpacity onPress={() => navigation.navigate(registerName)}>
                            <Text style={{ fontSize: 18, color: 'blue' }}>Register</Text>
                        </TouchableOpacity>
                    </View>

                </View>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
}

const styles = StyleSheet.create({
    container: { // for keyboard-avoiding-view
        flex: 1,
        paddingTop: StatusBar.currentHeight,
    },
    inner: { // for inner view
        flex: 1,
        alignItems: 'center',
        // justifyContent: 'center',
    },
    logo: {
        width: '40%',
        height: '40%',
    },
    textInput: { // for username and password
        width: 200,
        height: 35,
        borderColor: '#000000',
        borderBottomWidth: 1,
        marginBottom: 20,
    },
    textInputWithNoMarginBottom: {
        marginBottom: 0,
    },
})

export default SigninScreen;