import 'package:flutter/material.dart';
import 'package:math_memorator/screens/home_screen.dart';
import 'package:math_memorator/screens/real_numbers_screen.dart';
import 'package:math_memorator/screens/functions_screen.dart';
import 'package:math_memorator/screens/progressions_screen.dart';
import 'package:math_memorator/screens/complex_numbers.dart';
import 'package:math_memorator/screens/enumeration_screen.dart';
import 'package:math_memorator/screens/vectors.dart';
import 'package:math_memorator/screens/analytics.dart';
import 'package:math_memorator/screens/trigonometry.dart';
import 'package:math_memorator/screens/matrices.dart';
import 'package:math_memorator/screens/composition_rules.dart';
import 'package:math_memorator/screens/functions_limits.dart';
import 'package:math_memorator/screens/derivates.dart';
import 'package:math_memorator/screens/integrals.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(

        primarySwatch: Colors.blue,

        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomeScreen(),
        routes: {
          '' : (_) => HomeScreen(),
          RealNumbersScreen.route: (_) => RealNumbersScreen(),
          ProgressionsScreen.route: (_) => ProgressionsScreen(),
          FunctionsScreen.route: (_) => FunctionsScreen(),
          ComplexNumbersScreen.route: (_) => ComplexNumbersScreen(),
          EnumerationScreen.route: (_) => EnumerationScreen(),
          VectorsScreen.route: (_) => VectorsScreen(),
          AnalyticsScreen.route: (_) => AnalyticsScreen(),
          TrigonometryScreen.route: (_) => TrigonometryScreen(),
          MatricesScreen.route: (_) => MatricesScreen(),
          CompositionRulesScreen.route: (_) => CompositionRulesScreen(),
          FunctionsLimitsScreen.route: (_) => FunctionsLimitsScreen(),
          DerivatesScreen.route: (_) => DerivatesScreen(),
          IntegralsScreen.route: (_) => IntegralsScreen(),
        },
    );
  }
}