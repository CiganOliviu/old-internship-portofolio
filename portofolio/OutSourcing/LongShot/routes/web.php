<?php


use Illuminate\Support\Facades\Route;
use App\Http\Controllers\IndexController;
use App\Http\Controllers\BandNewsController;
use App\Http\Controllers\TourController;

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

Route::get('/', [IndexController::class, 'IndexView'])->name("IndexView");
Route::post('newsletter-data', [IndexController::class, 'SaveDataToNewsletterTableViews'])->name('SaveDataToNewsletterTableViews');

Route::get('band-news', [BandNewsController::class, 'BandNewsView'])->name('BandNewsView');
Route::get('tour', [TourController::class, 'TourView'])->name('TourView');
