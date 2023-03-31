import React from 'react';
import axios from 'axios';
import {
    StyleSheet, View, Text, TextInput, Button, Image, StatusBar, KeyboardAvoidingView,
    TouchableWithoutFeedback, Keyboard, TouchableOpacity
} from 'react-native';
import Logo from '../../assets/logo.png';
import Global from '../navigation/Global';

function SigninScreen(props) {
    const { navigation } = props;
    const [username, onChangeUsername] = React.useState('');
    const [password, onChangePassword] = React.useState('');

    const handleSignin = async (username, password) => {
        const session_url = 'http://172.20.10.3:5000/users/signin';
    
        axios.post(session_url, {
            "username": username,
            "password": password
        })
            .then(response => {
                if (response.status === 200) { // signin successful
                    navigation.navigate(Global.innerName);
                    onChangeUsername('');
                    onChangePassword('');
                    console.log(`User ${response.data.user.username} has successfully logged in.`);
                    // console.log(response.data.user); // logs user info from db
                } 
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

                        <TouchableOpacity style={{ alignSelf: 'flex-end' }} onPress={() => navigation.navigate(Global.forgotPasswordName)}>
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
                        <TouchableOpacity onPress={() => navigation.navigate(Global.registerName)}>
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