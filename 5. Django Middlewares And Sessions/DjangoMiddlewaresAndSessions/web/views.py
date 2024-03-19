import time
from time import sleep

from django.shortcuts import render
from django.views import generic as views


class MeasureExecutionTime:
    def dispatch(self, request, *args, **kwargs):
        # Code before the request
        start_time = time.time()

        dispatch_result = super().dispatch(request, *args, **kwargs)

        # Code after the
        end_time = time.time()
        print(f"Executed in {start_time - end_time} seconds") 

        return dispatch_result


class IndexView(MeasureExecutionTime, views.TemplateView):
    template_name = 'web/index.html'

    def context_data(self, **kwargs):
        load_count = self.request.session.get("load_count", 0)

        self.request.session["load_count"] = load_count + 1

        context = super().get_context_data(**kwargs)

        context["load_count"] = self.request.session["load_count"]

        return context