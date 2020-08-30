import 'package:flutter/material.dart';

import 'package:math_memorator/screens/main_drawer.dart';
import 'package:math_memorator/screens/home_screen.dart';

class RealNumbersScreen extends StatelessWidget {

  static const route = '/real-numbers-screen';

  @override
  Widget build(BuildContext context) {

    return Scaffold (
      appBar: AppBar (
        title: Text("Numere Reale"),
      ),

      drawer: MainDrawer(),

      body: Center (
        child: Column (
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Numere Reale",
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