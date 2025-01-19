## Table of contents
* [General info](#general-info)
* [Test Methods](#test-methods)
  * [1. test_add_new_book_add_two_books](#1-test_add_new_book_add_two_books)
  * [2. test_add_new_book_add_one_book_book_added](#2-test_add_new_book_add_one_book_book_added)
  * [3. test_add_new_book_add_one_book_not_added](#3-test_add_new_book_add_one_book_not_added)
  * [4. test_set_book_genre_set_existing_genre_genre_set](#4-test_set_book_genre_set_existing_genre_genre_set)
  * [5. test_set_book_genre_set_not_existing_genre_genre_not_set](#5-test_set_book_genre_set_not_existing_genre_genre_not_set)
  * [6. test_get_book_genre_get_genre_genre_correct](#6-test_get_book_genre_get_genre_genre_correct)
  * [7. test_get_books_with_specific_genre_get_book_with_genre_list_correct](#7-test_get_books_with_specific_genre_get_book_with_genre_list_correct)
  * [8. test_get_books_for_children_get_child_books_list_correct](#8-test_get_books_for_children_get_child_books_list_correct)
  * [9. test_add_book_in_favorites_add_one_book_book_added](#9-test_add_book_in_favorites_add_one_book_book_added)
  * [10. test_add_book_in_favorites_add_same_book_book_not_added](#10-test_add_book_in_favorites_add_same_book_book_not_added)
  * [11. test_delete_book_from_favorites_remove_one_book_book_removed](#11-test_delete_book_from_favorites_remove_one_book_book_removed)
  * [12. test_get_list_of_favorites_books_get_list_list_returned](#12-test_get_list_of_favorites_books_get_list_list_returned)

## General info
This project is created to test class BooksCollector.
	
## Test Methods
You can find all test methods in [tests.py](../blob/main/tests.py)
  
### 1. test_add_new_book_add_two_books
The test is created to verify *add_new_book* method with adding 2 books.

### 2. test_add_new_book_add_one_book_book_added
The test is created to verify *add_new_book* method with adding 1 book.

### 3. test_add_new_book_add_one_book_not_added
The test is created to verify 2 negative scenarios for *add_new_book* method when adding 1 book.

### 4. test_set_book_genre_set_existing_genre_genre_set
The test is created to verify *set_book_genre* method when setting an existing genre.

### 5. test_set_book_genre_set_not_existing_genre_genre_not_set
The test is created to verify *set_book_genre* method when setting not existing genre.

### 6. test_get_book_genre_get_genre_genre_correct
The test is created to verify *get_book_genre* method.

### 7. test_get_books_with_specific_genre_get_book_with_genre_list_correct
The test is created to verify *get_books_with_specific_genre* method.

### 8. test_get_books_for_children_get_child_books_list_correct
The test is created to verify *get_books_for_children* method.

### 9. test_add_book_in_favorites_add_one_book_book_added
The test is created to verify *add_book_in_favorites* method.

### 10. test_add_book_in_favorites_add_same_book_book_not_added
The test is created to verify *add_book_in_favorites* method when adding the same book to Favourites.

### 11. test_delete_book_from_favorites_remove_one_book_book_removed
The test is created to verify *delete_book_from_favorites* method.

### 12. test_get_list_of_favorites_books_get_list_list_returned
The test is created to verify *get_list_of_favorites_books* method.