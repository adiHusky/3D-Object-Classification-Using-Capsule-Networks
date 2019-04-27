<?php include 'header.php'; ?>
	<section class="hero d-flex align-items-center p-relevtive">

		<div class="container">
			<!-- <div class="row">
				<div class="col-md-10 col-md-offset-1">
					<p class="small-text-hero"><i class="icon-localizer text-primary mr-1"></i>Lorem ipsum <span class="text-primary">dolor sit</span> amet</p>
					<h1>Let's <span class="text-primary">go </span> anywhere</h1>
					<p class="text-hero">Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
				</div>
			</div> -->
			<div class="row">
				<div class="col-md-10 col-lg-10 col-sm-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1">
					<div class="search-bar m-all">
						<form action="grid.php" method="GET">
              <div class="row">
                <div class="form-group col-lg-10  col-sm-10 col-md-10">
                  <input type="search" name="" class="new-control" id="autocomplete" placeholder="Browse by category?">

                  <input type="hidden" name="term" class="new-control" id="term" placeholder="Browse by category?">
                  <input type="hidden" name="keyword" class="new-control" id="keyword" placeholder="What are you searching for?">

                </div>
                <div class="form-group col-lg-2  col-sm-2 col-md-2"><br>
                  <button type="submit" class="bg-transparent">
                  <i class="fa fa-search text-primary fa-3x" aria-hidden="true"></i>
                  </button>
                </div>
              </div>
            </form>
					</div>
				</div>
			</div>
			<div class="p-absolute" style="display: none;	">
				<div class="col-md-12">
					<div class="row">
						<div class="col-md-3"><img height="50px" class="img-rounded" src="http://www.mindblowingpsychology.com/wp-content/uploads/2018/01/Square-Faces-300x300.jpg"></div>
						<div class="col-md-9"><p class="text-muted">officia deserunt mollit anim id est laborum.</p></div>
					</div>
					<div class="row">
						<div class="col-md-3"><img height="50px" class="img-rounded" src="http://www.mindblowingpsychology.com/wp-content/uploads/2018/01/Square-Faces-300x300.jpg"></div>
						<div class="col-md-9"><p class="text-muted">officia deserunt mollit anim id est laborum.</p></div>
					</div>
					<div class="row">
						<div class="col-md-3"><img height="50px" class="img-rounded" src="http://www.mindblowingpsychology.com/wp-content/uploads/2018/01/Square-Faces-300x300.jpg"></div>
						<div class="col-md-9"><p class="text-muted">officia deserunt mollit anim id est laborum.</p></div>
					</div>
				</div>
			</div>
		</div>
	</section>



</body>
</html>

<script type="text/javascript">
  $( function() {

 // Single Select
 $( "#autocomplete" ).autocomplete({
  source: function( request, response ) {
   // Fetch data
   $.ajax({
    url: "fetchData.php",
    type: 'post',
    dataType: "json",
    data: {
     search: request.term
    },
    success: function( data ) {
     response( data );
    }
   });
  },
  select: function (event, ui) {
   // Set selection/*
   $('#autocomplete').val(ui.item.label);
    // display the selected text
    $('#keyword').val(ui.item.label);
   $('#term').val(ui.item.catId); // save selected id to input*/
  return false;
  }
 });

 // Multiple select
 $( "#multi_autocomplete" ).autocomplete({
    source: function( request, response ) {
                
      var searchText = extractLast(request.term);
      $.ajax({
         url: "fetchData.php",
         type: 'post',
         dataType: "json",
         data: {
           search: searchText
         },
         success: function( data ) {
           response( data );
         }
       });
    },
    select: function( event, ui ) {
        var terms = split( $('#multi_autocomplete').val() );
                
        terms.pop();
                
        terms.push( ui.item.label );
                
        terms.push( "" );
        $('#multi_autocomplete').val(terms.join( ", " ));

        // Id
        terms = split( $('#selectuser_ids').val() );
                
        terms.pop();
                
        terms.push( ui.item.value );
                
        terms.push( "" );
        $('#selectuser_ids').val(terms.join( ", " ));

        return false;
     }
           
 });

});
function split( val ) {
   return val.split( /,\s*/ );
}
function extractLast( term ) {
   return split( term ).pop();
}
</script>