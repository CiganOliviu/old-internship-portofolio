<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {

    return view('home');
});

Route::get('/sediums', function () {

    return view('sediums');
});

Route::get('/industries', function () {

    return view('industries');
});

Route::get('/events', function () {

    return view('events');
});

Route::get('/jobs', function () {

    return view('jobs');
});

Route::get('/blog', function () {

    return view('blog');
});

Route::get('/contact', function () {

    return view('contact');
});
