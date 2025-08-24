
window.addEventListener('DOMContentLoaded', () => {
	// Get Specified Elements
	const childs = document.getElementsByClassName("string-separator")
	
	// Each width synchronized to its parent
	for (var child_index = 0; child_index < childs.length; child_index++) {
		var each_child = childs[child_index];
		
		var each_child_styles = window.getComputedStyle(each_child);
		
		var each_child_width = each_child_styles.width;
		
		var each_parent = each_child.parentElement;
		
		each_parent.style.width = each_child_width;
  	
	}

});
