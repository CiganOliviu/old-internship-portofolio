import 'package:flutter/material.dart';

import 'package:math_memorator/screens/main_drawer.dart';
import 'package:math_memorator/screens/home_screen.dart';

class EnumerationScreen extends StatelessWidget {

  static const route = '/enumeration-screen';

  @override
  Widget build(BuildContext context) {

    return Scaffold (
      appBar: AppBar (
        title: Text("Enumeration"),
      ),

      drawer: MainDrawer(),

      body: Center (
        child: Column (
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Enumeration",
              style: TextStyle(fontSize: 22, ),),
          ],
        ),
      ),

      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.home),
        onPressed: () {
          Navigator.of(context).pushNamed(HomeScreen.route);
        },
      ),

    );
  }
}