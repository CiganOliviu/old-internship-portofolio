import 'package:flutter/material.dart';
import 'package:math_memorator/screens/real_numbers_screen.dart';
import 'package:math_memorator/screens/functions_screen.dart';
import 'package:math_memorator/screens/progressions_screen.dart';
import 'package:math_memorator/screens/complex_numbers.dart';
import 'package:math_memorator/screens/enumeration_screen.dart';
import 'package:math_memorator/screens/trigonometry.dart';
import 'package:math_memorator/screens/vectors.dart';
import 'package:math_memorator/screens/analytics.dart';
import 'package:math_memorator/screens/matrices.dart';
import 'package:math_memorator/screens/composition_rules.dart';
import 'package:math_memorator/screens/functions_limits.dart';
import 'package:math_memorator/screens/derivates.dart';
import 'package:math_memorator/screens/integrals.dart';

class MainDrawer extends StatelessWidget {

  @override
  Widget build(BuildContext context) {

    return Drawer(
        child: ListView (
          padding: EdgeInsets.zero,
          children: <Widget>[
            Container (
              width: double.infinity,
              padding: EdgeInsets.all(20),
              color: Theme.of(context).primaryColor,
              child: Center (
                child: Column (
                  children: <Widget>[
                    Container(
                      width: 100,
                      height: 100,
                      margin: EdgeInsets.only(
                        top: 30,
                      ),
                      decoration: BoxDecoration (
                        shape: BoxShape.circle,
                        image: DecorationImage (image: NetworkImage(
                            'https://s3.amazonaws.com/static.graphemica.com/glyphs/i500s/000/002/768/original/03A3-500x500.png?1275292566'
                          ),
                          fit: BoxFit.fill
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Numere Reale',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(RealNumbersScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Progresii',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(ProgressionsScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Functii',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(FunctionsScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Numere Complexe',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(ComplexNumbersScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Metode de numarare',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(EnumerationScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Vectori in plan',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(VectorsScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Geometrie Analitica',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(AnalyticsScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Trigonometrie',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(TrigonometryScreen.route);
              },
            ),


            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Matrice',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(MatricesScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Legi de Compozitie',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(CompositionRulesScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Limite de functii',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(FunctionsLimitsScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Derivate',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(DerivatesScreen.route);
              },
            ),

            ListTile(
              leading: Icon(Icons.folder),
              title: Text('Integrale',
                style: TextStyle (
                  fontSize: 18,
                ),
              ),
              onTap: () {
                Navigator.of(context).pop();
                Navigator.of(context).pushNamed(IntegralsScreen.route);
              },
            ),

          ],
        ),
      );
  }
}