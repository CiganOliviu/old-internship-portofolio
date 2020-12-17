<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class BandNews extends Model
{

    protected $BandNewsTable = 'BandNews';

    protected $fillable = ['title', 'introduction', 'description', 'image', 'author'];
}
