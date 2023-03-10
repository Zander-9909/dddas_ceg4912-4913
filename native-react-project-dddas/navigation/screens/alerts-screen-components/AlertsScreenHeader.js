import React from "react";
import { Text, StyleSheet } from "react-native";

function AlertsScreenHeader() {
  return(
    <Text style={styles.text}>
      DDDAS Alerts
    </Text>
  );
}

const styles = StyleSheet.create({
  text: {
    fontSize: 35,
    height: '10%',
    top: '0%',
    width: '100%',
    backgroundColor: 'red',
    textAlign: 'center',
    textAlignVertical: 'center'
  },
})

export default AlertsScreenHeader;