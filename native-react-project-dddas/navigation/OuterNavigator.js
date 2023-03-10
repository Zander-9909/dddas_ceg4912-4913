import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';

// screens
import ForgotPasswordScreen from './auth-screens/ForgotPasswordScreen';
import LoginScreen from './auth-screens/LoginScreen';
import RegisterScreen from './auth-screens/RegisterScreen';
import NavigationScreen from './screens/NavigationScreen';
import InnerNavigator from './InnerNavigator';

// screen names
const forgotPasswordName = 'ForgotPassword';
const loginScreenName = 'Login';
const registerName = 'Register';
const navigationName = 'Navigation';

const Stack = createStackNavigator();

function OuterNavigator() {
	return (
		<Stack.Navigator
			screenOptions={{}}
			initialRouteName={loginScreenName}>

			<Stack.Screen name={loginScreenName} component={LoginScreen} />
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