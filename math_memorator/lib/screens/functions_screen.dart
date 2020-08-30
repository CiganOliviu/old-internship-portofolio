import 'package:flutter/material.dart';

import 'package:math_memorator/screens/main_drawer.dart';
import 'package:math_memorator/screens/home_screen.dart';

class FunctionsScreen extends StatelessWidget {

  static const route = '/functions-screen';

  @override
  Widget build(BuildContext context) {

    return Scaffold (
      appBar: AppBar (
        title: Text("Functii"),
      ),

      drawer: MainDrawer(),

      body: Center (
        child: Column (
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Functii",
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