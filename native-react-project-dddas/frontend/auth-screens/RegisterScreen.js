import React from 'react';
import {
    StyleSheet, Text, View, TouchableWithoutFeedback, KeyboardAvoidingView, StatusBar,
    TextInput, Keyboard, Button, Image
} from 'react-native';
import Logo from '../../assets/logo.png';
import Global from '../navigation/Global';

function RegisterScreen(props) {
    const { navigation } = props;
    const [firstName, onChangeFirstName] = React.useState('');
    const [lastName, onChangeLastName] = React.useState('');
    const [username, onChangeUsername] = React.useState('');
    const [email, onChangeEmail] = React.useState('');
    const [password, onChangePassword] = React.useState('');

    const handleRegister = async () => {
        const session_url = 'http://192.168.0.7:5000/users/add';

        axios.post(session_url, {
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password
        })
            .then(response => {
                if (response.status === 200) { // register successful
                    navigation.navigate(Global.signinScreenName);
                    onChangeFirstName('');
                    onChangeLastName('');
                    onChangeUsername('');
                    onChangeEmail('');
                    onChangePassword('');
                    console.log(`User has been registered.`);
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

                    <View style={styles.logoContainer}>
                        <Image
                            style={styles.logo}
                            source={Logo}
                            resizeMode='contain'
                        />
                        <Text style={styles.baseText}>
                            CREATE NEW ACCOUNT
                        </Text>
                    </View>

                    <View style={styles.inputContainer}>
                        <TextInput
                            style={styles.textInput}
                            onChangeText={onChangeFirstName}
                            value={firstName}
                            placeholder='First Name'

                            keyboardType='default'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
                        <TextInput
                            style={styles.textInput}
                            onChangeText={onChangeLastName}
                            value={lastName}
                            placeholder='Last Name'

                            keyboardType='default'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
                        <TextInput
                            style={styles.textInput}
                            onChangeText={onChangeUsername}
                            value={username}
                            placeholder='Username'

                            keyboardType='default'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
                        <TextInput
                            style={styles.textInput}
                            onChangeText={onChangeEmail}
                            value={email}
                            placeholder='Email Address'

                            keyboardType='email-address'
                            spellCheck={false}
                            autoCorrect={false}
                            maxLength={20}
                        />
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
                            onPress={() => handleRegister}
                            title='CREATE NEW ACCOUNT'
                        />
                    </View>

                </View>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
}

const styles = StyleSheet.create({
    baseText: {
        // flex: 0.5,
        fontSize: 18,
        fontWeight: 'bold',
        // marginTop: '5%',
    },
    buttonMargin: {
        marginBottom: '25%'
    },
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
    logo: {
        // flex: 3,
        width: '40%',
        height: '80%', // logo will occupy 80% of the 38% of the screen = 30.4%
        // marginTop: '15%',
    },
    logoContainer: {
        width: '100%',
        height: '38%', // logo and 'create new account' will occupy 38% of screen
        alignItems: 'center',
        justifyContent: 'center',
    },
    textInput: { // for username and password
        width: 200,
        height: 35,
        borderColor: '#000000',
        borderBottomWidth: 1,
        marginBottom: 10,
    },
})

export default RegisterScreen;