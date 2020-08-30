import 'package:flutter/material.dart';

import 'package:math_memorator/screens/main_drawer.dart';
import 'package:math_memorator/screens/home_screen.dart';

class DerivatesScreen extends StatelessWidget {

  static const route = '/derivates-screen';

  @override
  Widget build(BuildContext context) {

    return Scaffold (
      appBar: AppBar (
        title: Text("Derivate"),
      ),

      drawer: MainDrawer(),

      body: Center (
        child: Column (
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Derivate",
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