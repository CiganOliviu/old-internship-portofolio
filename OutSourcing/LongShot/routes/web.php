<?php


use App\Http\Controllers\TourAdministrationController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\IndexController;
use App\Http\Controllers\BandNewsController;
use App\Http\Controllers\TourController;
use App\Http\Controllers\AuthenticationController;
use App\Http\Controllers\BandNewsAdministrationController;

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

Route::get('login', [AuthenticationController::class, 'LoginView'])->name('LoginView');
Route::post('login/check-login', [AuthenticationController::class, 'CheckLogin'])->name('CheckLogin');
Route::get('administration', [AuthenticationController::class, 'SuccessLoginView'])->name('SuccessLoginView');
Route::get('logout', [AuthenticationController::class, 'LogoutView'])->name('LogoutView');

Route::get('band-news-administration', [BandNewsAdministrationController::class, 'BandNewsAdministrationView'])->name("BandNewsAdministrationView");
Route::post('band-news-data', [BandNewsAdministrationController::class, 'SaveDataToBandNewsTableViews'])->name('SaveDataToBandNewsTableViews');

Route::get('tour-administration', [TourAdministrationController::class, 'TourAdministrationView'])->name("TourAdministrationView");
Route::post('tour-data', [TourAdministrationController::class, 'SaveDataToTourTableViews'])->name('SaveDataToTourTableViews');
