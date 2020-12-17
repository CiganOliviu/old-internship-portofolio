<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateBandNewsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('band_news', function (Blueprint $table) {
            $table->id();
            $table->string('title')->default("");
            $table->string('introduction')->default("");
            $table->mediumText('description')->default("");
            $table->string('image')->default("");
            $table->string('author')->default("");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('band_news');
    }
}
