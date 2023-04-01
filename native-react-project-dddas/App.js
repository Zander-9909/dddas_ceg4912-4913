import React from 'react';
import OuterNavigator from './frontend/navigation/OuterNavigator.js'
import { NavigationContainer } from '@react-navigation/native';

import SettingsNavigator from './frontend/navigation/SettingsNavigator.js';
import InnerNavigator from './frontend/navigation/InnerNavigator.js';

export default function App(props) {
	return (
		<NavigationContainer>
			<OuterNavigator/>
			{/* <SettingsNavigator/> */}
			{/* <InnerNavigator/> */}
		</NavigationContainer>
	);
}

