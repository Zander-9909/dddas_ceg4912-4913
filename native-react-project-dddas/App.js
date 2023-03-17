import React from 'react';
import OuterNavigator from './frontend/navigation/OuterNavigator.js'
import { NavigationContainer } from '@react-navigation/native';


export default function App(props) {
	return (
		<NavigationContainer>
			<OuterNavigator />
		</NavigationContainer>
	);
}

