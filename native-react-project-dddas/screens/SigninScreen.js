import React from 'react';
import {
    StyleSheet, View, Text, TextInput, Button, Image, StatusBar, KeyboardAvoidingView,
    TouchableWithoutFeedback, Keyboard, TouchableOpacity
} from 'react-native';
import Logo from 'C:/Users/downt/Documents/GitHub/dddas_ceg4912-4913/native-react-project-dddas/assets/Logo.png';


// screen names
const forgotPasswordName = 'ForgotPassword';
const registerName = 'Register';
const navigationName = 'HomeScreen';

function SigninScreen(props) {
    const { navigation } = props;
    const [username, onChangeUsername] = React.useState('');
    const [password, onChangePassword] = React.useState('');

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

                        {/* <TouchableOpacity style={{ alignSelf: 'flex-end' }} onPress={() => navigation.navigate(forgotPasswordName)}>
                            <Text style={{ fontSize: 18, color: 'blue' }}>Forgot password?</Text>
                        </TouchableOpacity> */}
                    </View>

                    <View style={{ marginBottom: '20%' }}>
                        <Button
                            color='blue'
                            onPress={() => navigation.navigate(navigationName)}
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