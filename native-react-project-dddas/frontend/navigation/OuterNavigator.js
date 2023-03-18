import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';

// screens
import ForgotPasswordScreen from '../auth-screens/ForgotPasswordScreen';
import SigninScreen from '../auth-screens/SigninScreen';
import RegisterScreen from '../auth-screens/RegisterScreen';
import InnerNavigator from './InnerNavigator';
import Global from './Global';

const Stack = createStackNavigator();

function OuterNavigator() {
	return (
		<Stack.Navigator
			screenOptions={{}}
			initialRouteName={Global.signinScreenName}>

			<Stack.Screen name={Global.signinScreenName}
				component={SigninScreen}
				options={{
					headerShown: false,
					title: 'Sign in',
				}}
			/>
			<Stack.Screen name={Global.registerName} component={RegisterScreen} />
			<Stack.Screen name={Global.forgotPasswordName} component={ForgotPasswordScreen} />
			<Stack.Screen
				name={Global.innerName}
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