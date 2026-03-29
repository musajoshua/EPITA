package com.musajoshua.todoproject

import android.os.Bundle
import android.widget.EditText
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val todoTextInput = findViewById<EditText>(R.id.todoInput)
        val todoSubmitButton = findViewById<Button>(R.id.todoSubmit)
        val todoTitleText = findViewById<TextView>(R.id.todoTitle)


        todoSubmitButton.setOnClickListener() {
            val userInput = todoTextInput.text.toString()

            todoTitleText.text = userInput

            println(userInput)
        }
    }
}