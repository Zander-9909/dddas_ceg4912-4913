import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';

// screens
import ForgotPasswordScreen from '../auth-screens/ForgotPasswordScreen';
import SigninScreen from '../auth-screens/SigninScreen';
import RegisterScreen from '../auth-screens/RegisterScreen';
import InnerNavigator from './InnerNavigator';

// screen names
const forgotPasswordName = 'ForgotPassword';
const signinScreenName = 'Signin';
const registerName = 'Register';
const navigationName = 'Navigation';

const Stack = createStackNavigator();

function OuterNavigator() {
	return (
		<Stack.Navigator
			screenOptions={{}}
			initialRouteName={signinScreenName}>

			<Stack.Screen name={signinScreenName}
				component={SigninScreen}
				options={{
					headerShown: false,
					title: 'Sign in',
				}}
			/>
			<Stack.Screen name={registerName} component={RegisterScreen} />
			<Stack.Screen name={forgotPasswordName} component={ForgotPasswordScreen} />
			<Stack.Screen
				name={navigationName}
				component={InnerNavigator}
				options={{
					headerShown: false, // hide the top bar when navigating from outer to inner
					gestureEnabled: false // cannot swipe back from inner to outer navigations
				}}
			/>

		</Stack.Navigator>
	);
}

export default OuterNavigator;