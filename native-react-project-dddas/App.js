import React from "react";
import InnerNavigator from "./navigation/InnerNavigator";
import OuterNavigator from "./navigation/OuterNavigator";
import { NavigationContainer } from '@react-navigation/native';


export default function App(props) {
	return (
		<NavigationContainer>
			<OuterNavigator />
		</NavigationContainer>

	);
}

