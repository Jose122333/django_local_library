from django.shortcuts import render
from .models import ITOperation, ITManagement,ITGovernance, Document,CorpGovernance
from django.contrib.auth.decorators import login_required

from .forms import DocumentForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


@login_required
def dFogIT(request):

    ops = ITOperation.objects.all()[0]
    manag = ITManagement.objects.all()[0]
    gov = ITGovernance.objects.all()[0]
    corp = CorpGovernance.objects.all()[0]


    # Render list page with the documents and the form
    return render(
        request,
        'catalog/dfogit.html',
        context={'ITOperation':ops,
                'ITManagement':manag,
                'ITGovernance':gov,
                'CorpGovernance':corp}
            )
