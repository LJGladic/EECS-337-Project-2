# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo

import requests
from bs4 import BeautifulSoup
while True:
    requested_recipe_webpage = ''
    requested_recipe = ''
    user_response = input('Do you have a recipe number? (y/n): ')
    if user_response == 'y':
        while True:
            recipe_number = input('Please enter the recipe number: ')
            requested_recipe_webpage = 'https://www.allrecipes.com/recipe/'
            requested_recipe_webpage += recipe_number
            requested_recipe = requests.get(requested_recipe_webpage)
            if requested_recipe.status_code == 200:
                break
            else:
                print("There was an error fetching that recipe number, please make sure it is correct")
        break
    elif user_response == 'n':
        while True:
            requested_recipe_webpage = input('Please enter any allrecipes.com recipe URL: ')
            requested_recipe = requests.get(requested_recipe_webpage)
            if requested_recipe.status_code == 200:
                break
            else:
                print('There was an error fetching the recipe, please make sure the URL was correct')
        break
    else:
        print('Input not valid, please try again.')

soup = BeautifulSoup(requested_recipe.text, 'html.parser')
#print (soup)
# print(soup.title)

# gets title
recipe_tital = soup.find("h1", {"id": "recipe-main-content"}).text
print(recipe_tital)
#soup.find_all("div", class_="stylelistrow")
recipe_time = soup.find("span", class_="ready-in-time").text
# requested_recipe has the content from the website
print(recipe_time)

prep_times = soup.find_all("li", class_="prepTime__item")
# for p in prep_times:
#     print(p)

ingredients = soup.find_all("span", class_="recipe-ingred_txt added")
ingredients_lst = []
for i in ingredients:
    ingredients_lst.append(i.text)
    print(i.text)

directions = soup.find_all("span", class_="recipe-directions__list--item")
directions_lst = []
for d in directions:
    directions_lst.append(d.text)
    print (d.text)
# div summary background  for title and short description

# title = id =recipe_main_content
# can get stars


#calories , time , serving
# <span class="recipe-ingredients__header__toggles">
#     <span class="ready-in-time__container">
#         <span class="ready-in-time" aria-label="Ready in 1 Hour 10 Minutes">1 h 10 m</span>
#         <span class="svg-icon--recipe-page--time_stats_gr svg-icon--recipe-page--time_stats_gr-dims"></span>
#     </span>
#
#     <meta id="metaRecipeServings" itemprop="recipeYield" content="24">
#
#     <a href="" id="servings-button" class="servings-adust-trigger" popup-trigger="servingsSection">
#         <span class="servings-count" ng-class="{'active': servingsSection_showing}"><span ng-bind="adjustedServings" class="ng-binding">24</span><span class="servings-count__desc" ng-class="{'active': servingsSection_showing}"> servings</span></span>
#
#         <span class="svg-icon--recipe-page--servings_gr svg-icon--recipe-page--servings_gr-dims" ng-class="{'active': servingsSection_showing}"></span>
#     </a>
#
#         <a href="" id="nutrition-button" class="nutrition-trigger" data-scroll-to-anchor="nutrition-info" onclick="AnchorScroll('nutrition-info');segmentRecipeAnalyticsTrack('Calories Clicked')">
#             <span class="calorie-count" aria-label="238 calories"><span>238</span> <span class="calorie-count__desc" aria-hidden="true"> cals</span></span>
#             <span class="svg-icon--recipe-page--nutrition_gr svg-icon--recipe-page--nutrition_gr-dims"></span>
#         </a>
# </span>


# direction
# <section class="recipe-directions ng-scope" data-ng-controller="ar_controllers_recipe_notes" data-ng-init="init(6969, 'recipe', 1)">
#     <h2 class="heading__h2--gutters">
#         Directions
#     </h2>
#     <span class="recipe-directions__header--toggles" id="recipe-notes">
#     <span class="recipe-notes" ng-show="displayNote">
#         <a href="" ng-click="openNoteModal()" aria-label="Add Personal Note">
#             <span class="note-text ng-binding">Add a note</span>
#             <span class="svg-icon--actions--edit_icon svg-icon--actions--edit_icon-dims"></span>
#         </a>
#     </span>
#
#
#         <span class="recipe-directions--print"><a ng-href="https://www.allrecipes.com/recipe/6969/peach-bread/print?recipeType=Recipe&amp;servings=24&amp;isMetric=false" aria-label="Printer-friendly View" data-internal-referrer-link="recipe button" data-click-id="recipe button" class="recipe-print-toggle-btn ng-isolate-scope" target="_self" href="https://www.allrecipes.com/recipe/6969/peach-bread/print?recipeType=Recipe&amp;servings=24&amp;isMetric=false"><span class="kf-text print">Print</span> <span class="svg-icon--recipe-navbar--print svg-icon--recipe-navbar--print-dims"></span></a></span>
#
#
#     </span>
#
#     <div class="directions--section">
#         <div class="directions--section__steps ng-scope" ng-controller="ar_controllers_directions" ng-init="init(6969, 1)">
#             <!-- cooking stats -->
#     <ul class="prepTime">
#         <li class="prepTime__item"><span class="svg-icon--recipe-page--time_stats_gr svg-icon--recipe-page--time_stats_gr-dims"></span></li>
#         <li class="prepTime__item" aria-label="Prep time: 10 Minutes">
#             <p class="prepTime__item--type" aria-hidden="true">Prep</p><time itemprop="prepTime" datetime="PT10M"><span aria-hidden="true"><span class="prepTime__item--time">10</span> m</span></time>
#         </li>
#                     <li class="prepTime__item" aria-label="Cook time: 1 Hour ">
#                 <p class="prepTime__item--type" aria-hidden="true">Cook</p><time itemprop="cookTime" datetime="PT1H"><span aria-hidden="true"><span class="prepTime__item--time">1</span> h</span></time>
#             </li>
#                     <li class="prepTime__item" aria-label="Ready in 1 Hour 10 Minutes">
#                 <p class="prepTime__item--type" aria-hidden="true">Ready In</p><time itemprop="totalTime" datetime="PT1H10M"><span aria-hidden="true"><span class="prepTime__item--time">1</span> h <span class="prepTime__item--time">10</span> m</span></time>
#             </li>
#     </ul>
#
#
#             <ol class="list-numbers recipe-directions__list" itemprop="recipeInstructions">
#                         <li class="step" ng-class="{'finished': stepIsActive0}" ng-click="biTracking(stepIsActive0 = !stepIsActive0)">
#                             <span class="recipe-directions__list--item">Preheat oven to 350 degrees F (175 degrees C).   Grease and flour two 8 x 4 inch loaf pans.
#                             </span>
#                         </li>
#                         <li class="step" ng-class="{'finished': stepIsActive1}" ng-click="biTracking(stepIsActive1 = !stepIsActive1)">
#                             <span class="recipe-directions__list--item">In a large bowl, beat the eggs lightly.  Blend in the sugar, oil, and vanilla.  Add flour, baking powder, baking soda, salt, and cinnamon; mix just to combine. Stir in the peaches and nuts.  Pour batter into prepared pans.
#                             </span>
#                         </li>
#                         <li class="step" ng-class="{'finished': stepIsActive2}" ng-click="biTracking(stepIsActive2 = !stepIsActive2)">
#                             <span class="recipe-directions__list--item">Bake for about 1 hour, or until a tester inserted in the center comes out clean.
#                             </span>
#                         </li>
#             </ol>
#             <a href="" ng-click="openNoteModal()" aria-label="Add Personal Note">
#                 <ol class="list-numbers recipe-directions__list recipeNotes ng-hide" ng-show="model.itemNote">
#                     <li class="step">
#                         <span class="recipe-directions__list--item ng-binding" ng-bind="model.itemNote"></span>
#                     </li>
#                 </ol>
#             </a>
#             <div id="karma-lazy-seriesDetails"></div>
#         </div>
#         <div class="directions--section__right-side">
#             <div class="directions--section__tipsAndTricks">
# <div class="directions--section__tipsAndTricks__title">
#     <span class="directions--section__tipsAndTricks__title__font">You might also like</span>
# </div>
# <div class="relatedVideos">
#             <div class="relatedVideos__item">
#                 <a href="https://www.allrecipes.com/video/673/banana-banana-bread/?internalSource=tips and tricks&amp;referringId=6969&amp;referringContentType=Recipe&amp;clickId=tips and tricks 1" data-internal-referrer-link="tips and tricks" data-click-id="tips and tricks 1" class="ng-isolate-scope" target="_self">
#                     <img class="relatedVideos__thumbnail ng-isolate-scope" data-lazy-load="" data-original-src="https://cf-images.us-east-1.prod.boltdns.net/v1/static/1033249144001/0ebabff6-3872-4b38-ad70-898e0c409522/5c06ad95-8591-41bb-a768-f6fd965ae3d3/160x90/match/image.jpg" alt="" title="" src="https://cf-images.us-east-1.prod.boltdns.net/v1/static/1033249144001/0ebabff6-3872-4b38-ad70-898e0c409522/5c06ad95-8591-41bb-a768-f6fd965ae3d3/160x90/match/image.jpg">
#                 </a>
#                 <div class="relatedVideos__thumbnail__icon-hasVideo">
#                     <a class="icon--videoplay ng-isolate-scope" href="https://www.allrecipes.com/video/673/banana-banana-bread/?internalSource=tips and tricks&amp;referringId=6969&amp;referringContentType=Recipe&amp;clickId=tips and tricks 1" data-internal-referrer-link="tips and tricks" data-click-id="tips and tricks 1" target="_self"></a>
#                 </div>
#                 <div class="relatedVideos__details">
#                     <a href="https://www.allrecipes.com/video/673/banana-banana-bread/?internalSource=tips and tricks&amp;referringId=6969&amp;referringContentType=Recipe&amp;clickId=tips and tricks 1" data-internal-referrer-link="tips and tricks" data-click-id="tips and tricks 1" class="ng-isolate-scope" target="_self">
#                         <span class="relatedVideos__details_title">Banana Banana Bread</span>
#                         <p class="relatedVideos__details__description">With this much banana flavor, it just had to be called “banana banana.”</p>
#                     </a>
#                 </div>
#             </div>
#
# </div>
#             </div><div class="bxc bx-base bx-custom bx-active-step-1 bx-campaign-917327 bx-width-default bx-type-agilityzone bx-has-close-x-1 bx-impress" id="bx-campaign-917327" style="display: none; visibility: hidden; margin-top: 0px; margin-left: 0px;"><div id="bx-shroud-917327" class="bx-matte bx-shroud bx-shroud-917327"></div><div id="bx-hover-shroud-917327" class="bx-hover-shroud bx-hover-shroud-917327" style="display:none"></div><div class="bx-slab"><div class="bx-align"><div class="bx-creative bx-creative-917327" id="bx-creative-917327"><div class="bx-wrap"><a id="bx-close-inside-917327" class="bx-close bx-close-link bx-close-inside" href="javascript:void(0)" data-click="close"><svg class="bx-close-xsvg" viewBox="240 240 20 20"><g class="bx-close-xstroke bx-close-x-adaptive"><path class="bx-close-x-adaptive-1" d="M255.6 255.6l-11.2-11.2" vector-effect="non-scaling-stroke"></path><path class="bx-close-x-adaptive-2" d="M255.6 244.4l-11.2 11.2" vector-effect="non-scaling-stroke"></path></g></svg><div class="bx-ally-label">close dialog</div></a><div class="bx-step bx-step-1 bx-active-step bx-step-NpRWRQT bx-step-917327-1 bx-tail-placement-hidden" id="bx-step-917327-1" data-close-placement=""><form id="bx-form-917327-step-1" bx-novalidate="true" method="post" action="https://api.bounceexchange.com/capture/submit" onsubmit="return bouncex.submitCampaignStep(917327); return false" onreset="bouncex.close_ad(917327); return false"><input type="hidden" name="campaign_id" value="917327"><div class="bx-group bx-group-custom bx-group-917327-4NqQzf5 bx-group-4NqQzf5" id="bx-group-917327-4NqQzf5"><a href="https://www.magazine.store/allrecipes-magazine/?utm_source=allrecipes&amp;utm_medium=internal&amp;utm_campaign=i811trkw1256df" target="" class="" data-click="hyperlink"></a></div><div class="bx-group bx-group-default bx-group-917327-bqBNQgm bx-group-bqBNQgm" id="bx-group-917327-bqBNQgm"><div class="bx-row bx-row-text bx-row-text-default  bx-row-45d7WZQ bx-element-917327-45d7WZQ" id="bx-element-917327-45d7WZQ"><div>Get the magazine</div></div></div><div class="bx-group bx-group-default bx-group-917327-oybETjY bx-group-oybETjY" id="bx-group-917327-oybETjY"><div class="bx-row bx-row-text bx-row-text-default  bx-row-MsTedRv bx-element-917327-MsTedRv" id="bx-element-917327-MsTedRv"><div>Get a full year for just $10!</div></div><div class="bx-row bx-row-text bx-row-text-default  bx-row-3ml4dZ6 bx-element-917327-3ml4dZ6" id="bx-element-917327-3ml4dZ6"><div>Cook 5-star weekday dinners every time. </div></div></div></form></div></div></div></div></div><a id="bx-close-outside-917327" class="bx-close bx-close-link bx-close-outside" href="javascript:void(0)" data-click="close"><svg class="bx-close-xsvg" viewBox="240 240 20 20"><g class="bx-close-xstroke bx-close-x-adaptive"><path class="bx-close-x-adaptive-1" d="M255.6 255.6l-11.2-11.2" vector-effect="non-scaling-stroke"></path><path class="bx-close-x-adaptive-2" d="M255.6 244.4l-11.2 11.2" vector-effect="non-scaling-stroke"></path></g></svg><div class="bx-ally-label">close dialog</div></a><style id="bx-campaign-917327-style">/* effects for .bx-campaign-917327 *//* custom css .bx-campaign-917327 *//* custom css from creative 32872 */.bx-custom.bx-campaign-917327 .bx-group > a {    display: block;    height: 100%;}@media screen and (max-width:736px) {    #bx-group-917327-jrJy3A1,    #bx-group-917327-tonMitu {        padding-top:20px;    }}/* rendered styles .bx-campaign-917327 */.bxc.bx-campaign-917327.bx-active-step-1 .bx-creative> *:first-child {width: 300px;padding: 0px;vertical-align: top;}.bxc.bx-campaign-917327.bx-active-step-1 .bx-creative:before {min-height: 122px;}.bxc.bx-campaign-917327.bx-active-step-1 .bx-creative {background-color: white;background-image: url(//assets.bounceexchange.com/assets/uploads/clients/2602/creatives/e939b09dc272026b89d85e65910cb56b.jpg);background-position: 4% 80%;background-size: 60px;}.bxc.bx-campaign-917327 .bx-group-917327-4NqQzf5 {width: 300px;position: absolute;top: 0;left: 0;height: 100%;z-index: 50;cursor: pointer;}.bxc.bx-campaign-917327 .bx-group-917327-bqBNQgm {padding: 0;}.bxc.bx-campaign-917327 .bx-element-917327-45d7WZQ {text-align: left;padding: 0;}.bxc.bx-campaign-917327 .bx-element-917327-45d7WZQ> *:first-child {font-family: "Source Sans Pro", Arial;font-weight: 300;font-style: italic;font-size: 17px;color: #2d2d2d;line-height: 1.3em;padding: 4px 0 0 7px;}.bxc.bx-campaign-917327 .bx-group-917327-oybETjY {padding: 10px 0 0 81px;text-align: left;}.bxc.bx-campaign-917327 .bx-element-917327-MsTedRv {text-align: left;padding: 0 0 4px 0;}.bxc.bx-campaign-917327 .bx-element-917327-MsTedRv> *:first-child {font-family: "Source Sans Pro", Arial;font-weight: 400;font-style: normal;font-size: 14px;color: #4d4d4d;line-height: 1.3em;}.bxc.bx-campaign-917327 .bx-element-917327-3ml4dZ6 {text-align: left;width: 88%;}.bxc.bx-campaign-917327 .bx-element-917327-3ml4dZ6> *:first-child {font-family: "Source Sans Pro", Arial;font-weight: 300;font-style: normal;font-size: 12px;color: grey;line-height: 18px;}</style></div>
#             <div class="mag-cta-desktop" style="display: none;">
#                 <div class="mag-cta ng-scope" data-ng-controller="ar_controllers_mag_subscription">
#
#     <a ng-href="http://armagazine.com/get-the-magazine" target="_blank" class="ad-mag-homeBtm" href="http://armagazine.com/get-the-magazine">
#         <h2>Get the magazine</h2>
#         <img class="ad-mag-homeBtm__th ng-isolate-scope" data-lazy-load="" data-original-src="https://images.media-allrecipes.com/images/86146.png" alt="Subscribe to Allrecipes Magazine" title="Allrecipes Magazine" src="https://images.media-allrecipes.com/ar/spacer.gif">
#         <div class="ad-mag-homeBtm__text">
#             <h4>Get a full year for $5!</h4>
#             <p>Cook 5-star weekday dinners every time.</p>
#         </div>
#     </a>
# </div>
#             </div>
#         </div>
#     </div>
# </section>
