import React from 'react';
import {
    StyleSheet, View, Text, TextInput, Button, Image, StatusBar, KeyboardAvoidingView,
    TouchableWithoutFeedback, Keyboard
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

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
            style={styles.container}>
            <StatusBar backgroundColor="#FFFFFF" barStyle="dark-content" />

            <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                <View style={styles.inner}>
                    <Image
                        style={styles.logo}
                        source={Logo}
                        resizeMode='contain'
                    />

                    <TextInput
                        style={styles.textInput}
                        onChangeText={onChangeUsername}
                        value={username}
                        placeholder='Username'
                        keyboardType='default'

                        autoCorrect={false}
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
                        maxLength={20}
                    />

                    <Button
                        onPress={() => navigation.navigate(forgotPasswordName)}
                        title='Forgot Password'
                        style={{}}
                    />

                    <Button
                        onPress={() => navigation.navigate(registerName)}
                        title='Register'
                        style={{}}
                    />

                    <Button
                        onPress={() => navigation.navigate(navigationName)}
                        title='Sign in'
                        style={{}}
                    />
                </View>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        paddingTop: StatusBar.currentHeight,
    },
    inner: {
        flex: 1,
        alignItems: 'center',
        // justifyContent: 'center',
    },
    logo: {
        width: '40%',
        height: '40%',
    },
    textInput: {
        width: 200,
        height: 40,
        borderColor: '#000000',
        borderBottomWidth: 1,
        marginBottom: 20,
    },
    textInputWithNoMarginBottom: {
        marginBottom: 0, // Override the marginBottom property for this input
    },
})

export default SigninScreen;