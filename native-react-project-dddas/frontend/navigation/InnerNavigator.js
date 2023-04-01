import * as React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons'

// screens
import NavigationScreen from '../screens/NavigationScreen';
import AlertsScreen from '../screens/AlertsScreen';
import StatsScreen from '../screens/StatsScreen';
import Global from './Global';
import SettingsNavigator from './SettingsNavigator';

const Tab = createBottomTabNavigator();

function InnerNavigator() {
    return (
        <Tab.Navigator
            initialRouteName={Global.navigationName}
            screenOptions={({ route }) => ({
                // tab bar style
                headerShown: false, // hides header
                tabBarActiveTintColor: 'tomato',
                tabBarInactiveTintColor: 'grey',

                // tab bar icon select
                tabBarIcon: ({ focused, color, size }) => {
                    let iconName;
                    let rn = route.name;
                    // https://ionic.io/ionicons/
                    switch (rn) {
                        case Global.navigationName:
                            iconName = focused ? 'home' : 'home-outline';
                            break;
                        case Global.alertsName:
                            iconName = focused ? 'list' : 'list-outline';
                            break;
                        case Global.statsName:
                            iconName = focused ? 'stats-chart' : 'stats-chart-outline';
                            break;
                        case Global.settingsNavName:
                            iconName = focused ? 'settings' : 'settings-outline';
                            break;
                    }
                    return <Ionicons name={iconName} size={size} color={color} />

                },
            })}>

            <Tab.Screen name={Global.navigationName} component={NavigationScreen} />
            <Tab.Screen name={Global.alertsName} component={AlertsScreen} />
            <Tab.Screen name={Global.statsName} component={StatsScreen} />
            <Tab.Screen name={Global.settingsNavName} component={SettingsNavigator} />

        </Tab.Navigator>
    );
}

export default InnerNavigator;
