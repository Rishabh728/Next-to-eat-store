// search nav 

const searchContainer = document.getElementById('nav_search_custom-search-container');
        const searchBar = document.getElementById('nav_search_custom-search-bar');
        const searchIcon = document.getElementById('nav_search_custom-search-icon');
        const userCart = document.getElementById('user_cart');
        const searchSubmit = document.getElementById('nav_search_custom-search-submit');

        searchIcon.addEventListener('click', () => {
            searchContainer.classList.toggle('active');
            userCart.classList.toggle('hidden');
            if (searchContainer.classList.contains('active')) {
                searchBar.querySelector('input').focus();
                searchBar.style.cssText = "border: 0.1px solid #ccc;  ";  
                searchIcon.style.display = "none"
                // Close the search bar when clicking outside
                document.addEventListener('click', function(event) {
                if (!searchBar.contains(event.target) && event.target !== searchIcon) {
                    searchBar.style.display = 'none';
                    window.location.reload();
                }
 });

            }
            else {
                searchBar.style.border = "none"
                
            }
        });

 
     // Prevent clicks inside the search bar from closing it
     searchBar.addEventListener('click', function(event) {
        event.stopPropagation();
     });
       // Submit search when clicking the submit button
    searchSubmit.addEventListener('click', function() {
        alert('Searching for: ' + searchInput.value);
        searchBar.style.display = 'none'; // Hide the search bar after submitting
        searchInput.value = ''; // Clear the input field
    });
      
   // Add the sticky class when user scrolls down
window.onscroll = function() {
    var navbar = document.querySelector('.navbar');
  
    if (window.scrollY > 1) {
      navbar.classList.add('sticky');
    } else {
      navbar.classList.remove('sticky');
    }
  };
  