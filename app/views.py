from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import  CreateView, UpdateView
import pickle
from django.http import FileResponse, HttpResponse, HttpResponseBadRequest



class HomePageView(TemplateView):
    template_name = 'index.html'


class CausesPreventionView(TemplateView):
    template_name = 'causes_prevention.html'


class SymptomsView(TemplateView):
    template_name = 'symptoms.html'


class TreamtmentView(TemplateView):
    template_name = 'treatment.html'




class CadPredictionView(TemplateView):
    template_name = 'cadform.html'




class CadStagePredictionView(TemplateView):
    template_name = 'stageform.html'




def predict_cad(request):
    try:
        with open('detectcad.pkl', 'rb') as file:
            model = pickle.load(file)
        # Convert inputs to float
        age = float(request.GET.get('age', 0.0))
        sex = float(request.GET.get('gender', 0.0))
        chest_pain_type = float(request.GET.get('chest_pain_type', 0.0))
        rest_blood_press = float(request.GET.get('rest_blood_press', 0.0))
        cholesterol = float(request.GET.get('cholesterol', 0.0))
        fasting_blood_sugar = float(request.GET.get('fasting_blood_sugar', 0.0))
        restecg = float(request.GET.get('restecg', 0.0))
        max_heart_rate = float(request.GET.get('max_heart_rate', 0.0))
        exer_ind_angina = float(request.GET.get('exer_ind_angina', 0.0))
        st_depression = float(request.GET.get('st_depression', 0.0))
        st_slope = float(request.GET.get('st_slope', 0.0))
        num_major_vessels = float(request.GET.get('num_major_vessels', 0.0))
        thallium_scint = float(request.GET.get('thallium_scint', 0.0))

        # Make prediction
        cad_prediction_result = model.predict([[age, sex, chest_pain_type, rest_blood_press, cholesterol, 
            fasting_blood_sugar, restecg, max_heart_rate, exer_ind_angina, 
            st_depression, st_slope, num_major_vessels, thallium_scint]])

        # Interpret prediction result
        result_dict = {"output": 0} if cad_prediction_result[0] == 0 else {"output": 1}
        return render(request, 'cadform.html', {'result': result_dict})
    except FileNotFoundError:
        return HttpResponseBadRequest('Model file not found')
    except ValueError:
        return HttpResponseBadRequest('Invalid input data')



def predict_cad_stage(request):
    try:
        with open('stagecad.pkl', 'rb') as file:
            model = pickle.load(file)
        # Convert inputs to float
        age = float(request.GET.get('age', 0.0))
        sex = float(request.GET.get('gender', 0.0))
        chest_pain_type = float(request.GET.get('chest_pain_type', 0.0))
        rest_blood_press = float(request.GET.get('rest_blood_press', 0.0))
        cholesterol = float(request.GET.get('cholesterol', 0.0))
        fasting_blood_sugar = float(request.GET.get('fasting_blood_sugar', 0.0))
        restecg = float(request.GET.get('restecg', 0.0))
        max_heart_rate = float(request.GET.get('max_heart_rate', 0.0))
        exer_ind_angina = float(request.GET.get('exer_ind_angina', 0.0))
        st_depression = float(request.GET.get('st_depression', 0.0))
        st_slope = float(request.GET.get('st_slope', 0.0))
        num_major_vessels = float(request.GET.get('num_major_vessels', 0.0))
        thallium_scint = float(request.GET.get('thallium_scint', 0.0))

        # Make prediction
        cad_prediction_result = model.predict([[age, sex, chest_pain_type, rest_blood_press, cholesterol, 
            fasting_blood_sugar, restecg, max_heart_rate, exer_ind_angina, 
            st_depression, st_slope, num_major_vessels, thallium_scint]])
        # Interpret prediction result
        if cad_prediction_result[0] == 0:
            result_dict = {"output": 0}
        elif cad_prediction_result[0] == 1:
            result_dict = {"output": 1}
        elif cad_prediction_result[0] == 2:
            result_dict = {"output": 2}
        elif cad_prediction_result[0] == 3:
            result_dict = {"output": 3}
        elif cad_prediction_result[0] == 4:
            result_dict = {"output": 4}
        return render(request, 'stageform.html', {'result': result_dict})
    except FileNotFoundError:
        return HttpResponseBadRequest('Model file not found')
    except ValueError:
        return HttpResponseBadRequest('Invalid input data')


