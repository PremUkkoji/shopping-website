function displayModalView(str)
{
	var message = '['+str+']';
	try
    {
        var response = JSON.parse(message);
    }
    catch(err)
    {
        response = '"'+message.replace(/\\?"/g,'\\"')+'"';
        eval('response = '+response);
    }

    var bodyContent = "";
    for(product in response)
    {
    	bodyContent += '<div class="row">';
    	bodyContent += '<div class="col">';
    	bodyContent += '<article class="media content-section">';
    	bodyContent += '<img class="article-img" src="../../../../media/' + response[product].image + '">';
    	bodyContent += '<div class="media-body">';
    	bodyContent += '<h2 class="article-title">' + response[product].title + '</h2>';
    	bodyContent += '<small class="text-muted">₹' + response[product].sku.price.$numberDecimal + '</small>';
    	bodyContent += '</div>';
    	bodyContent += '<a class="btn btn-info btn-sm mt-1 mb-1" href="http://localhost:8000/add/'+ response[product] +'">Add to Cart</a>';
    	bodyContent += '</article>';
    	bodyContent += '</div>';
    	bodyContent += '</div>';
    	bodyContent += '<br/>';
    }
    document.getElementById("modalBody").innerHTML = bodyContent;
    // automatic appearing of model
    $('#myModal').modal('show');
}

function userMessage(userMessage)
{
	//creating p element with user message
		var p = document.createElement('p');
		p.className = 'float-right chat-message self-chat-message';
		var paraText = document.createTextNode(userMessage);
		p.appendChild(paraText);

		//creating div for p
		var colDiv = document.createElement('div');
		colDiv.className = 'col';
		colDiv.appendChild(p);

		//creating img with user pic
		var userpic = document.createElement('img');
		userpic.src = '/static/chatbot/images/avatar.png';

		//creating div for userpic
		var userPicDiv = document.createElement('div');
		userPicDiv.className = 'float-right user-photo';
		userPicDiv.appendChild(userpic);

		//creating div for userpic's div
		var userPicDivsDiv = document.createElement('div');
		userPicDivsDiv.className = 'col-1';
		userPicDivsDiv.appendChild(userPicDiv);

		//creating second last outermost div of new message
		var secondLastDiv = document.createElement('div');
		secondLastDiv.className = 'row flex-row-reverse';
		secondLastDiv.appendChild(userPicDivsDiv);
		secondLastDiv.appendChild(colDiv);

		//creating outermost div of new message
		var newmessage = document.createElement('div');
		newmessage.className = 'chat self container';
		newmessage.appendChild(secondLastDiv);

		//user message
		document.getElementById('chatlogs').appendChild(newmessage);
}

function isJson(msg)
{
	var str = '['+msg+']';
	var flag = 0;
	try
	{
		JSON.parse(str);
	}
    catch(err)
    {
    	response = '"'+str.replace(/\\?"/g,'\\"')+'"';
    	eval('response = '+response);
    	flag=1;
    }
    if(flag==1)
    {
    	try
    	{
    		JSON.parse(response);
    	}
    	catch(err)
    	{
    		return false;
    	}
    }
    return true;
}

function chatbotMessage(message)
{
	if(message)
	{
		//creating p element with user message
		var p = document.createElement('p');
		p.className = 'chat-message friend-chat-message';
		if(message === "cart items")
		{
			var a = document.createElement('a');
			a.setAttribute('href',"http://localhost:8000/cart/");
			a.innerHTML = "Click here to view Cart Items";
			p.appendChild(a);
		}
		else if(message === "purchased items")
		{
			var a = document.createElement('a');
			a.setAttribute('href',"http://localhost:8000/purchased/");
			a.innerHTML = "Click here to view Purchased Items";
			p.appendChild(a);
		}
		else if(message === "profile")
		{
			var a = document.createElement('a');
			a.setAttribute('href',"http://localhost:8000/profile/");
			a.innerHTML = "Click here to view User Profile";
			p.appendChild(a);
		}
		else if(!isJson(message))
		{
			var paraText = document.createTextNode(message);
			p.appendChild(paraText);
		}
		else
		{
			var paraText = document.createTextNode("...");
			p.appendChild(paraText);
			displayModalView(message);
		}

		//creating div for p
		var colDiv = document.createElement('div');
		colDiv.className = 'col';
		colDiv.appendChild(p);

		//creating img with user pic
		var userpic = document.createElement('img');
		userpic.src = '/static/chatbot/images/chatbot.png';

		//creating div for userpic
		var userPicDiv = document.createElement('div');
		userPicDiv.className = 'user-photo';
		userPicDiv.appendChild(userpic);

		//creating div for userpic's div
		var userPicDivsDiv = document.createElement('div');
		userPicDivsDiv.className = 'col-1';
		userPicDivsDiv.appendChild(userPicDiv);

		//creating second last outermost div of new message
		var secondLastDiv = document.createElement('div');
		secondLastDiv.className = 'row';
		secondLastDiv.appendChild(userPicDivsDiv);
		secondLastDiv.appendChild(colDiv);

		//creating outermost div of new message
		var newmessage = document.createElement('div');
		newmessage.className = 'chat friend container';
		newmessage.appendChild(secondLastDiv);

		//user message
		document.getElementById('chatlogs').appendChild(newmessage);
	}
	else
	{
		alert("Sorry but I didn't get you");
	}
}