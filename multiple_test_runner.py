import unittest

from ajax import AjaxPage
from button_and_alert import ButtonAlertPage
from click import ClickPage
from client_side_delay import ClientPage
from dynamic_id import DynamicPage
from hidden_layers import ZPage
from load_delay import DelayPage
from mouse_over import MouseoverPage
from overlapped_element import OverlappedElementPage
from progress_bar import ProgressbarPage
from sample_app import SampleAppPage
from scrollbars import ScrollbarsPage
from text_input import TextinputPage
from verify_text import VerifyTextPage
from visibility import VisibilityElementPage

ajax_cases = unittest.TestLoader().loadTestsFromTestCase(AjaxPage)
button_and_alert_cases = unittest.TestLoader().loadTestsFromTestCase(ButtonAlertPage)
click_cases = unittest.TestLoader().loadTestsFromTestCase(ClickPage)
client_side_delay_cases = unittest.TestLoader().loadTestsFromTestCase(ClientPage)
dynamic_id_cases = unittest.TestLoader().loadTestsFromTestCase(DynamicPage)
hidden_layers_cases = unittest.TestLoader().loadTestsFromTestCase(ZPage)
load_delay_cases = unittest.TestLoader().loadTestsFromTestCase(DelayPage)
mouse_over_cases = unittest.TestLoader().loadTestsFromTestCase(MouseoverPage)
overlapped_element_cases = unittest.TestLoader().loadTestsFromTestCase(OverlappedElementPage)
progress_bar_cases = unittest.TestLoader().loadTestsFromTestCase(ProgressbarPage)
sample_app_cases = unittest.TestLoader().loadTestsFromTestCase(SampleAppPage)
scrollbars_cases = unittest.TestLoader().loadTestsFromTestCase(ScrollbarsPage)
text_input_cases = unittest.TestLoader().loadTestsFromTestCase(TextinputPage)
verify_text_cases = unittest.TestLoader().loadTestsFromTestCase(VerifyTextPage)
visibility_cases = unittest.TestLoader().loadTestsFromTestCase(VisibilityElementPage)

test_suite = unittest.TestSuite(
    [
        ajax_cases,
        button_and_alert_cases,
        click_cases,
        client_side_delay_cases,
        dynamic_id_cases,
        hidden_layers_cases,
        load_delay_cases,
        mouse_over_cases,
        overlapped_element_cases,
        progress_bar_cases,
        sample_app_cases,
        scrollbars_cases,
        text_input_cases,
        verify_text_cases,
        visibility_cases
    ]
)

unittest.TextTestRunner(verbosity=2).run(test_suite)
